package menu;

import excel.beans.row.ExcelRowBeans;
import mysql.connector.Connector;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.poi.ss.usermodel.Cell;

import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;

public class ConnectorMenu {
    Logger log = LogManager.getLogger(ConnectorMenu.class);

    public ConnectorMenu(ArrayList<ExcelRowBeans> rows) {
        run(rows);
    }

    /**
     * Gets the instance of the Connector singleton and calls the insert, batchInsert function of the Connector class and tracks the
     * time of both inserts
     * @param rows Rows of the Excel file that will be stored in the database
     */
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
                    " Prozent_Fertigstellung, Datum_Endfixierung, Abteilung, Bemerkung) VALUES (?,?,?,?,?,?,?,?)", rows,
                    200);
            time = System.currentTimeMillis() - time;
            System.out.printf("Insertdauer (Batchweise): %sms\n", time);

            con.delete("DELETE FROM t_mpm_milestones");

            time = System.currentTimeMillis();
            con.storedInsert("{call batchInsert (?,?,?,?,?,?,?,?)}", rows,
                    200);
            time = System.currentTimeMillis() - time;
            System.out.printf("Insertdauer (Batchweise | Stored procedure): %sms\n", time);

        } catch (IOException | ClassNotFoundException | SQLException e) {
            log.error(e.getMessage());
        }
    }
}
