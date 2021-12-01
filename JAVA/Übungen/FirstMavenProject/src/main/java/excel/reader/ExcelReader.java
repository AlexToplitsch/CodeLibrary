package excel.reader;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.poi.hssf.extractor.ExcelExtractor;
import org.apache.poi.ss.usermodel.*;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

public class ExcelReader {
    // ############################# Properties ######################################
    Logger LOG = LogManager.getLogger(ExcelReader.class);
    String path;
    Workbook wb;
    Sheet sheet;
    Row row;
    Cell cell;
    InputStream input;


    // ############################# Constructor #####################################
    public ExcelReader(String path) {
        this.path = path;
    }


    // ############################# Getter/Setter  ####################################

    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public Workbook getWb() {
        return wb;
    }

    public void setWb(Workbook wb) {
        this.wb = wb;
    }

    public Sheet getSheet() {
        return sheet;
    }

    public void setSheet(Sheet sheet) {
        this.sheet = sheet;
    }

    public Row getRow() {
        return row;
    }

    public void setRow(Row row) {
        this.row = row;
    }

    public Cell getCell() {
        return cell;
    }

    public void setCell(Cell cell) {
        this.cell = cell;
    }


    // ############################# Functions #######################################

    /**
     *
     */
    public void readFile(int sheetIndex, int rowIndex, int cellIndex){
        if(createInputStream())
            if(createWorkbook())
                if(createSheet(sheetIndex))
                    if(createRow(rowIndex))
                        if(createCell(cellIndex))
                            LOG.info("Auslesen erfolgreich");
    }

    /**
     * Creates an FileInputStream with the file that is defined by the abstract path
     * @return boolean: True if file exists; False if file not exists;
     */
    private boolean createInputStream(){
        try{
            input = new FileInputStream(path);
            return true;
        }catch(FileNotFoundException fnfE){
            LOG.error("Datei unter: " + path + " wurde nicht gefunden!");
            LOG.error("Error: File not found at: " +path);
        }catch(SecurityException sE){
            LOG.error("Security Manager blockiert den Zugriff auf die Datei: " + path);
            LOG.error("Error: Security Manager blocks access on file: " +  path);
        }
        return false;
    }

    private boolean createWorkbook(){
        try {
            wb = WorkbookFactory.create(input);
            return true;
        } catch (IOException e) {
            LOG.error(e.getMessage());
            LOG.error("Error: " + e.getMessage());
        }
        return false;
    }

    private boolean createSheet(int index){
        try {
            sheet = wb.getSheetAt(index);
            return true;
        }catch (IllegalArgumentException iaE){
            LOG.error(iaE.getMessage());
            LOG.error("Error: " + iaE.getMessage());
        }
        return false;
    }

    private boolean createRow(int index){
        try {
            row = sheet.getRow(index);
            return true;
        }catch(Exception e){
            LOG.error(e.getMessage());
            LOG.error("Error: " + e.getMessage());
        }
        return false;
    }

    private boolean createCell(int index){
        try {
            cell = row.getCell(index);
            return true;
        }catch(Exception e){
            LOG.error(e.getMessage());
            LOG.error("Error: " + e.getMessage());
        }
        return false;
    }
}
