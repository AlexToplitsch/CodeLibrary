package com.company;

import excel.beans.row.ExcelRowBeans;
import menu.ConnectorMenu;
import menu.ExcelMenu;
import mysql.connector.Connector;
import org.apache.poi.ss.format.CellDateFormatter;

import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {
        ExcelMenu menu = new ExcelMenu();
        ConnectorMenu cMenu = new ConnectorMenu(menu.getRows());
    }
}
