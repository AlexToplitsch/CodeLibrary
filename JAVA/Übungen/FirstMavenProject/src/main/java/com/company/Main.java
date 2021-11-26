package com.company;

import Menu_GUI.FileCopyMenu;
import com.fasterxml.jackson.databind.JsonNode;
import json.JSONReader;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;


public class Main {
    public static void main(String[] args) {
        /*
        CalculatorMenu.main();
        FileCopyMenu.main();
        */
        StringBuilder jsonSRC = new StringBuilder();
        String data = "";
        try {
            BufferedReader reader = new BufferedReader(new  FileReader(
                    "assets/SampleJson.txt"));
            do{
                jsonSRC.append(data);
                data = reader.readLine();
            }while(data != null);
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            JSONReader.deserialising(jsonSRC.toString());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
