package mysql.connector;

import jdk.nashorn.internal.codegen.CompilerConstants;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.ini4j.Ini;

import java.io.FileReader;
import java.io.IOException;
import java.sql.*;

//todo: Inline documentation
public class Connector {
    //####################### Properties #################################
    Logger log = LogManager.getLogger(Connector.class);
    private static Connector connector = null;
    private Connection con;
    private Ini ini;
    private String host;
    private String db;
    private String user;
    private String password;
    private CallableStatement cStmt;
    private Statement stmt;
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

    public boolean insert(String sql) {
        try {
            if (connect()) {
                Statement stmt = con.createStatement();
                stmt.execute(sql);
                log.debug("Insert statement successfully executed!");
                return true;
            } else {
                log.error("No connection available!");
            }
        } catch (SQLException e) {
            log.error(e.getMessage());
            log.error(sql);
        }
        return false;
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

    public void delete(String sql) throws SQLException{
        if (connect()) {
            Statement stmt = con.createStatement();
            stmt.execute(sql);
            log.debug("Delete statement successfully executed!");
        } else {
            throw new SQLException("No connection to Database available!");
        }
    }

    public void callStatement(String sql) throws SQLException{
        CallableStatement stmt = con.prepareCall(sql);
    }


    //######################### Private Functions ################################
    private boolean connect() {
        if(connected) return true;
        try {
            this.con = DriverManager.getConnection("jdbc:mysql://" + this.host + "/" + this.db, this.user, this.password);
            log.debug("Successfully connected to Database: " + this.host + "/" + this.db);
            connected = true;
            return true;
        } catch ( SQLException e0) {
            log.error(e0.getMessage());
            log.error("Error: " + e0.getMessage());
        }
        return false;
    }

    private void readConfigFile() throws IOException {
        this.ini = new Ini(new FileReader("src/main/resources/config.ini"));
        Ini.Section conf = ini.get("DATABASE");
        this.host = conf.get("host");
        this.db = conf.get("database");
        this.user = conf.get("user");
        this.password = conf.get("password");
        log.debug("Successfully read ini file!");
    }

    private void createStatement() throws SQLException{
        stmt = con.createStatement();
    }

    private void createCallableStatement() throws SQLException{
        cStmt = con.prepareCall("{call demoSp(?, ?)}");
    }
}

