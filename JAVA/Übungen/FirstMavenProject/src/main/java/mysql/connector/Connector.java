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

    /**
     * @return the instance of this class due to singleton purposes
     * @throws IOException            if not config file could not be located
     * @throws ClassNotFoundException if the Class of the jdbc drive is not found
     */
    public static Connector getInstance() throws IOException, ClassNotFoundException {
        if (connector == null) {
            connector = new Connector();
        }
        return connector;
    }

    /**
     * Inserts the values passed in the Cell array by executing the passed sql statement
     *
     * @param sql   the statement that will be executed (values in the sql statement has to be in question marks)
     *              eq: insert into ... Values (?,?,?,...)
     * @param cells the values for the statement; size of array has to be the same as the number of question marks
     */
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

    /**
     * Inserts the rows passed in the ArrayList that is passed. The amount of rows that are inserted, depends on the passed
     * batchSize.
     *
     * @param sql       the statement that will be executed (values in the sql statement has to be in question marks)
     *                  eq: insert into ... Values (?,?,?,...)
     * @param rows      the rows that will be inserted into the database
     * @param batchSize size of the batch (amount of rows that are inserted at once)
     */
    public void batchInsert(String sql, ArrayList<ExcelRowBeans> rows, int batchSize) {
        try {
            if (connect()) {
                PreparedStatement stmt = con.prepareStatement(sql);
                int counter = 0;
                for (ExcelRowBeans row : rows) {
                    try {
                        prepareBatchInsert(new Cell[]{row.getID_Zeile(), row.get$Projektbezeichnung(),
                                row.getZeilenbezeichnung(), row.getStart(), row.getProzent_Fertigstellung(),
                                row.getDatum_Endfixierung(), row.getAbteilung(), row.getBemerkungen()}, stmt);
                        stmt.addBatch();
                        counter++;
                        if (counter == batchSize || rows.indexOf(row) == rows.size() - 1) {
                            counter = 0;
                            stmt.executeBatch();
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

    /**
     * @param sql the command that is executed
     * @return The ResultSet of a sql select command
     * @throws SQLException if there is an error in your sql syntax or some issues with the database
     */
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

    /**
     * Performs the delete command that is passed
     *
     * @param sql the command that is executed
     * @throws SQLException if there is an error in your sql syntax or some issues with the database
     */
    public void delete(String sql) throws SQLException {
        if (connect()) {
            Statement stmt = con.createStatement();
            stmt.execute(sql);
            log.debug("Delete statement successfully executed!");
        } else {
            throw new SQLException("No connection to Database available!");
        }
        try {
            con.close();
        } catch (SQLException e) {
            log.error(e.getMessage());
        }

    }

    /**
     * Executes the passed stored procedure batch wise
     *
     * @param sql       the call statement of the stored procedures
     * @param rows      the rows that will be inserted
     * @param batchSize row count, that will be inserted at once
     */
    public void storedInsert(String sql, ArrayList<ExcelRowBeans> rows, int batchSize) {
        try {
            if (connect()) {
                CallableStatement stmt = con.prepareCall(sql);
                int counter = 0;
                for (ExcelRowBeans row : rows) {
                    try {
                        prepareBatchInsert(new Cell[]{row.getID_Zeile(), row.get$Projektbezeichnung(),
                                row.getZeilenbezeichnung(), row.getStart(), row.getProzent_Fertigstellung(),
                                row.getDatum_Endfixierung(), row.getAbteilung(), row.getBemerkungen()}, stmt);
                        stmt.addBatch();
                        counter++;
                        if (counter == batchSize || rows.indexOf(row) == rows.size() - 1) {
                            counter = 0;
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
        } finally {
            try {
                con.close();
            } catch (SQLException e) {
                log.error(e.getMessage());
            }
        }

    }


    //######################### Private Functions ################################

    /**
     * Builds a connection to the database
     *
     * @return true if it is connected, false if no connection is available
     */
    private boolean connect() {

        try {
            if(con.isClosed()) {
                this.con = DriverManager.getConnection("jdbc:mysql://" + this.host + "/" + this.db, this.user, this.password);
                log.debug("Successfully connected to Database: " + this.host + "/" + this.db);
                connected = true;
                return true;
            }
        } catch (SQLException e0) {
            log.error(e0.getMessage());
            log.error("Error: " + e0.getMessage());
        }
        return false;
    }

    /**
     * Reads the config.ini file from the recourse folder in the project folder and stores the data in the properties
     *
     * @throws IOException if the config file is not available
     */
    private void readConfigFile() throws IOException {
        Ini.Section conf = new Ini(new FileReader("src/main/resources/config.ini")).get("DATABASE");
        this.host = conf.get("host");
        this.db = conf.get("database");
        this.user = conf.get("user");
        this.password = conf.get("password");
        log.debug("Successfully read ini file!");
    }

    /**
     * Prepares and executes the passed sql statement
     *
     * @param sql   statement (has to be insert statement)
     * @param cells array of cells for value replacement
     * @throws SQLException if there is an error in the sql statement or something went wrong with the database
     */
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

    /**
     * Prepares the passed prepared statement
     * @param cells values for the insert statement
     * @param stmt the statement that will be prepared
     * @throws SQLException if something during the preparation goes wrong
     */
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

