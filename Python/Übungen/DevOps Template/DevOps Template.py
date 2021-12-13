#!/usr/bin/python3
# -*- python -*- ===============================================================================
#
#                      Copyright (C) KNAPP AG
#
#    The copyright to the computer program(s) herein is the property
#    of Knapp.  The program(s) may be used   and/or copied only with
#    the  written permission of  Knapp  or in  accordance  with  the
#    terms and conditions stipulated in the agreement/contract under
#    which the program(s) have been supplied.
#
# ===========================================================================================

import argparse
import urllib.parse

defProjects = {
    "1": "Customer Projects",
    "2": "Strategic Products"
}

defWIT = {
    "1": "Bug",
    "2": "Feature",
    "3": "Issue"
}

defDiscipline = {
    "0": "None",
    "1": "Development",
    "2": "Documentation",
    "3": "Integration",
    "4": "Specification",
    "5": "Test"
}

defStage = {
    "0": "None",
    "1": "Development",
    "2": "Production",
    "3": "Sandbox",
    "4": "Test"
}

template = '<table style="font-size:10pt;" width="100%" align=center> <tr> <td style="width: 10%; font-weight: bold; ' \
           'background-color: #d6d5d5; border: solid 1px">Repository</td> <td style="width: 40%; background-color: ' \
           '#f2f2f2; border: solid 1px">__REPO__</td> <td style="width: 10%; font-weight: bold; background-color: ' \
           '#d6d5d5; border: solid 1px">Branch</td> <td style="width: 40%; background-color: #f2f2f2; border: ' \
           'solid 1px">__BRANCH__</td> </tr> <tr> <td style="width: 10%; font-weight: bold; background-color: ' \
           '#d6d5d5; border: solid 1px">Server</td> <td style="width: 40%; background-color: #f2f2f2; border: ' \
           'solid 1px">__IP__</td> <td style="width: 10%; font-weight: bold; background-color: #d6d5d5; border: ' \
           'solid 1px">Traces</td> <td style="width: 40%; background-color: #f2f2f2; border: ' \
           'solid 1px">Directory or Attachment</td> </tr> </table> <p style="font-weight: bold">Solution</p> <p>&lt;' \
           'provided when resolved&gt;</p> <p style="font-weight: bold">Issue Description</p> <p>&lt;your description' \
           ' here&gt;</p> <p style="font-weight: bold">Expected Behavior</p> <p>&lt;your description here, optional ' \
           'link/hint to specifications&gt;</p> <p style="font-weight: bold">Examples</p> <p>&lt;Timestamp&gt;&lt;' \
           'OrderNr&gt;&lt;ToteNr&gt;&lt;LoadingUnitCode&gt;&lt;UserCode&gt;</p>'

linkParams = {}

# --------------------------------------------------------------------------------------------------
# Argument parsing
parser = argparse.ArgumentParser(description='Generate a DevOps link based on some imputs')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-e', '--extended', action='store_true', help='requests more field values than expected')
parser.add_argument('-p', '--public', action='store_true', help='Set the WorkItem as public')
parser.add_argument('-a', '--asta', action='store_true', help='Set the WorkItem as ASTA relevant')
parser.add_argument('-A', '--all-links', action='store_true', help='Generate the links for all supported workItemTypes')

args = parser.parse_args()


# --------------------------------------------------------------------------------------------------
## Function to get read in value
def getValue(valuename):
    return inputHandler("\n\tPlease enter the value for <" + valuename + ">: ")


# --------------------------------------------------------------------------------------------------
## Function to handle abortion during imput
def inputHandler(message):
    run = True
    while run:
        try:
            inputValue = input(message)
            run = False
        except KeyboardInterrupt:
            res = inputHandler("\n\tDo you really want to exit? y/n ")
            if res == 'y':
                exit(1)

    return inputValue


# --------------------------------------------------------------------------------------------------
## Function to read in from list
def getItem(lst, listname):
    print("\n\tSelect value for " + listname)
    run = True
    while run:
        for key in lst:
            print("\t" + key + " : " + lst[key])

        sel = inputHandler("\n\tPlease select number: ")
        if sel != None and sel != '':
            try:
                if lst[sel]:
                    run = False
            except:
                print("\tEnter valid key\n")

    return lst[sel]


# --------------------------------------------------------------------------------------------------
## Evaluate the input
linkProject = getItem(defProjects, "Project")
if args.all_links == False:
    linkWIT = getItem(defWIT, "WorkItemType")

linkParams["[Product]"] = "2505060 - KiSoft One"
linkParams["[Product version]"] = "V" + getValue("Product version <maj.min>")

# Parse ProjectInformations only in case of Customer Project
if linkProject == "Customer Projects":
    linkParams["[Functional location]"] = getValue("Functional location")
    linkParams["[Customer project number]"] = getValue("Customer project number")

# Etended handling
if args.extended == True:
    linkParams["[Title]"] = getValue("Title")
    linkParams["[Function number]"] = getValue("Function number")
    linkParams["[Discipline]"] = getItem(defDiscipline, "Discipline")
    linkParams["[Stage]"] = getItem(defStage, "Stage")
    linkParams["[Public]"] = "True" if args.public else "False"
    linkParams["[ASTA Relevant]"] = "True" if args.asta else "False"

    repo = getValue("Repository")
    template = template.replace("__REPO__", repo)

    branch = getValue("Branch")
    template = template.replace("__BRANCH__", branch)

    ip = getValue("Server-IP")
    template = template.replace("__IP__", ip)

print("\nCopy link to browser or save it as bookmark:\n")
if args.all_links == False:
    link = "https://dev.azure.com/KNAPP-Group/" + urllib.parse.quote(linkProject) \
           + "/_workitems/create/" + linkWIT + "?" + \
           urllib.parse.urlencode(linkParams, quote_via=urllib.parse.quote) + \
           "&" + urllib.parse.quote("[Repro steps]") + "=" + urllib.parse.quote_plus(template, safe='/<>')
    print(link)
else:
    for key in defWIT:
        link = "https://dev.azure.com/KNAPP-Group/" + urllib.parse.quote(linkProject) \
               + "/_workitems/create/" + defWIT[key] + "?" + \
               urllib.parse.urlencode(linkParams, quote_via=urllib.parse.quote) + \
               "&" + urllib.parse.quote("[Repro steps]") + "=" + urllib.parse.quote_plus(template, safe='/<>')
        print("\nLink for " + defWIT[key] + ":\n" + link)
