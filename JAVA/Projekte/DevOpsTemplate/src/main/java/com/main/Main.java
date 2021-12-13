package com.main;

import org.apache.commons.cli.*;

public class Main {
    public static void main(String[] args){
        Options options = new Options();
        options.addOption("v", false, " %(prog)s 1.0");
        CommandLineParser parser = new DefaultParser();
        try {
            CommandLine cmd = parser.parse(options, args);
        } catch (ParseException e) {
            e.printStackTrace();
        }
    }
}
