package mysql.connector;

import excel.beans.row.ExcelRowBeans;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.CellType;
import org.ini4j.Ini;

import java.io.FileReader;
import java.io.IOException;
import java.sql.*;
import java.util.ArrayList;

//todo: Inline documentation
public class Connector {
    //####################### Properties #################################
    Logger log = LogManager.getLogger(Connector.class);
    private static Connector connector = null;
    private Connection con;
    private String host;
    private String db;
    private String user;
    private String password;
    private boolean connected;


    //######################### Constructor ################################
    private Connector() throws IOException, ClassNotFoundException {
        Class.forName("com.mysql.cj.jdbc.Driver");
        readConfigFile();
    }


    //######################### Public Functions ################################
    public static Connector getInstance() throws IOException, ClassNotFoundException {
        if (connector == null) {
            connector = new Connector();
        }
        return connector;
    }

    public void insert(String sql, Cell[] cells) {
        try {
            if (connect()) {
                executeInsert(sql, cells);
                log.debug("Insert statement successfully executed!");
            } else {
                log.error("No connection available!");
            }
        } catch (SQLException e) {
            log.error(e.getMessage());
        }
    }

    public void batchInsert(String sql, ArrayList<ExcelRowBeans> rows) {
        try {
            if (connect()) {
                PreparedStatement stmt = con.prepareStatement(sql);
                int batchSize = 0;
                for (ExcelRowBeans row : rows) {
                    try {
                        prepareBatchInsert(new Cell[]{row.getID_Zeile(), row.get$Projektbezeichnung(),
                                row.getZeilenbezeichnung(), row.getStart(), row.getProzent_Fertigstellung(),
                                row.getDatum_Endfixierung(), row.getAbteilung(), row.getBemerkungen()}, stmt);
                        stmt.addBatch();
                        batchSize++;
                        if (batchSize == 50||rows.indexOf(row) == rows.size() -1) {
                            batchSize = 0;
                            stmt.executeBatch();
                            stmt.clearParameters();
                        }

                    } catch (SQLException e) {
                        log.error(e.getMessage());
                    }
                }
            } else {
                log.error("No connection available!");
            }
            log.debug("Insert statement successfully executed!");
        } catch (SQLException e) {
            log.error(e.getMessage());
        }
    }

    public ResultSet select(String sql) throws SQLException {
        if (connect()) {
            Statement stmt = con.createStatement();
            ResultSet res = stmt.executeQuery(sql);
            log.debug("Select statement successfully executed!");
            return res;
        } else {
            throw new SQLException("No connection to Database available!");
        }
    }

    public void delete(String sql) throws SQLException {
        if (connect()) {
            Statement stmt = con.createStatement();
            stmt.execute(sql);
            log.debug("Delete statement successfully executed!");
        } else {
            throw new SQLException("No connection to Database available!");
        }
    }

    public void callStatement(String sql) throws SQLException {
        CallableStatement stmt = con.prepareCall(sql);
    }


    //######################### Private Functions ################################
    private boolean connect() {
        if (connected) return true;
        try {
            this.con = DriverManager.getConnection("jdbc:mysql://" + this.host + "/" + this.db, this.user, this.password);
            log.debug("Successfully connected to Database: " + this.host + "/" + this.db);
            connected = true;
            return true;
        } catch (SQLException e0) {
            log.error(e0.getMessage());
            log.error("Error: " + e0.getMessage());
        }
        return false;
    }

    private void readConfigFile() throws IOException {
        Ini.Section conf = new Ini(new FileReader("src/main/resources/config.ini")).get("DATABASE");
        this.host = conf.get("host");
        this.db = conf.get("database");
        this.user = conf.get("user");
        this.password = conf.get("password");
        log.debug("Successfully read ini file!");
    }

    private void executeInsert(String sql, Cell[] cells) throws SQLException {
        PreparedStatement stmt = con.prepareStatement(sql);
        String proj = (cells[1] == null) ? null : cells[1].getStringCellValue();
        String row = (cells[2] == null) ? null : cells[2].getStringCellValue();
        Date date1 = (cells[3] == null || cells[3].getCellType() == CellType.BLANK) ? null : new Date(cells[3]
                .getDateCellValue().getTime());
        int percent = (cells[4] == null) ? -1 : (int) cells[4].getNumericCellValue();
        Date date2 = (cells[5] == null || cells[5].getCellType() == CellType.BLANK) ? null : new Date(cells[5]
                .getDateCellValue().getTime());
        String dep = (cells[6] == null) ? null : cells[6].getStringCellValue();
        String note = (cells[7] == null) ? null : cells[7].getStringCellValue();

        stmt.setInt(1, (int) cells[0].getNumericCellValue());
        stmt.setString(2, proj);
        stmt.setString(3, row);
        stmt.setDate(4, date1);
        stmt.setInt(5, percent);
        stmt.setDate(6, date2);
        stmt.setString(7, dep);
        stmt.setString(8, note);
        stmt.execute();
    }

    private void prepareBatchInsert(Cell[] cells, PreparedStatement stmt) throws
            SQLException {
        String proj = (cells[1] == null) ? null : cells[1].getStringCellValue();
        String row = (cells[2] == null) ? null : cells[2].getStringCellValue();
        Date date1 = (cells[3] == null || cells[3].getCellType() == CellType.BLANK) ? null : new Date(cells[3]
                .getDateCellValue().getTime());
        int percent = (cells[4] == null) ? -1 : (int) cells[4].getNumericCellValue();
        Date date2 = (cells[5] == null || cells[5].getCellType() == CellType.BLANK) ? null : new Date(cells[5]
                .getDateCellValue().getTime());
        String dep = (cells[6] == null) ? null : cells[6].getStringCellValue();
        String note = (cells[7] == null) ? null : cells[7].getStringCellValue();

        stmt.setInt(1, (int) cells[0].getNumericCellValue());
        stmt.setString(2, proj);
        stmt.setString(3, row);
        stmt.setDate(4, date1);
        stmt.setInt(5, percent);
        stmt.setDate(6, date2);
        stmt.setString(7, dep);
        stmt.setString(8, note);

    }
}

