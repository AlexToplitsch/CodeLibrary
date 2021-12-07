package com.company;

import excel.beans.row.ExcelRowBeans;
import menu.ExcelMenu;
import mysql.connector.Connector;
import org.apache.poi.ss.format.CellDateFormatter;

import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {
        ExcelMenu menu = new ExcelMenu();
        ArrayList<ExcelRowBeans> rows = menu.getRows();
        Connector con = null;
        try {
            con = Connector.getInstance();
            for (ExcelRowBeans row : rows) {
                con.insert(sqlBuilder(row));
            }


        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static String sqlBuilder(ExcelRowBeans row) {
        CellDateFormatter formatter = new CellDateFormatter("yyyy-MM-dd");
        String ID = "'" + (int) row.getID_Zeile().getNumericCellValue() + "'";
        String projekt = "'" + row.get$Projektbezeichnung() + "'";
        String zeilenbez = "'" + row.getZeilenbezeichnung() + "'";
        String start = (String.valueOf(row.getStart()).equals("")) ? "null" : "'" + row.getStart() + "'";
        String prozent = "'" + (int) row.getProzent_Fertigstellung().getNumericCellValue() + "'";
        String ende = (String.valueOf(row.getDatum_Endfixierung()).equals("")) ? "null" : "'" + row.getStart() + "'";
        String abteilung = "'" + row.getAbteilung() + "'";
        String bemerkung = "'" + row.getBemerkungen() + "'";
        return "Insert into " +
                "t_mpm_milestones (ID_ZEILE, Projektbezeichnung, Zeilenbezeichnung, Start_Datum" + ", Prozent_Fertigstellung," +
                " Datum_Endfixierung, Abteilung, Bemerkung)" +
                "VALUES(" + ID + ", " + projekt + ", " + zeilenbez + ", " + start + ", " + prozent + ", " + ende + ", " + abteilung + ", " +
                bemerkung + ")";
    }

}
