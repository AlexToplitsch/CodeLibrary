package menu;

import excel.beans.row.ExcelRowBeans;
import mysql.connector.Connector;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.poi.ss.format.CellDateFormatter;
import org.apache.poi.ss.usermodel.Cell;

import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;

//todo: Inline documentation
public class ConnectorMenu {
    Logger log = LogManager.getLogger(ConnectorMenu.class);

    public ConnectorMenu(ArrayList<ExcelRowBeans> rows) {
        run(rows);
    }

    private void run(ArrayList<ExcelRowBeans> rows) {
        Connector con;
        try {
            con = Connector.getInstance();

            long time = System.currentTimeMillis();
            for (ExcelRowBeans row : rows) {
                con.insert("Insert into t_mpm_milestones (ID, Projektbezeichnung, Zeilenbezeichnung, Start_Datum," +
                                " Prozent_Fertigstellung, Datum_Endfixierung, Abteilung, Bemerkung) VALUES (?,?,?,?,?,?,?,?)",
                        new Cell[]{row.getID_Zeile(), row.get$Projektbezeichnung(), row.getZeilenbezeichnung(), row.getStart(),
                                row.getProzent_Fertigstellung(), row.getDatum_Endfixierung(), row.getAbteilung(),
                                row.getBemerkungen()});
            }
            time = System.currentTimeMillis() - time;
            System.out.printf("Insertdauer (Zeilenweise): %sms\n", time);

            con.delete("DELETE FROM t_mpm_milestones");

            time = System.currentTimeMillis();
            con.batchInsert("Insert into t_mpm_milestones (ID, Projektbezeichnung, Zeilenbezeichnung, Start_Datum," +
                    " Prozent_Fertigstellung, Datum_Endfixierung, Abteilung, Bemerkung) VALUES (?,?,?,?,?,?,?,?)", rows);
            time = System.currentTimeMillis() - time;
            System.out.printf("Insertdauer (Batchweise): %sms\n", time);

        } catch (IOException | ClassNotFoundException| SQLException e) {
            log.error(e.getMessage());
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
                "t_mpm_milestones (ID, Projektbezeichnung, Zeilenbezeichnung, Start_Datum, Prozent_Fertigstellung," +
                " Datum_Endfixierung, Abteilung, Bemerkung)" +
                "VALUES(" + ID + ", " + projekt + ", " + zeilenbez + ", " + start + ", " + prozent + ", " + ende + ", " + abteilung + ", " +
                bemerkung + ")";
    }
}
