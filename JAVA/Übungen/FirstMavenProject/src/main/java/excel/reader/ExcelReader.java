package excel.reader;

import excel.beans.row.ExcelRowBeans;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.poi.EncryptedDocumentException;
import org.apache.poi.ss.usermodel.*;

import java.io.*;
import java.util.ArrayList;

public class ExcelReader {
    // ############################# Properties ######################################
    Logger LOG = LogManager.getLogger(ExcelReader.class);
    ArrayList<ExcelRowBeans> rows = new ArrayList<>();
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

    public ArrayList<ExcelRowBeans> getRows(){
        return rows;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public Workbook getWb() {
        return wb;
    }

    public void setWb() throws IOException, SecurityException {
        if (input == null) {
            createInputStream();
        }
        this.wb = WorkbookFactory.create(input);
    }

    public Sheet getSheet() {
        return sheet;
    }

    public void setSheet(int index) throws NullPointerException {
        if (wb == null) {
            throw new NullPointerException("Can't get sheet from not initialised Workbook");
        }
        this.sheet = wb.getSheetAt(index);
    }

    public void setSheet(String name) throws NullPointerException {
        if (wb == null) {
            throw new NullPointerException("Can't get sheet from not initialised Workbook");
        }
        this.sheet = wb.getSheet(name);
    }

    public Row getRow() {
        return row;
    }

    public void setRow(Row row) throws NullPointerException {
        if (sheet == null) {
            throw new NullPointerException("Can't get row from not initialised sheet");
        }
        this.row = row;
    }

    public Cell getCell() {
        return cell;
    }

    public void setCell(Cell cell) throws NullPointerException {
        if (row == null) {
            throw new NullPointerException("Can't get cell from not initialised row");
        }
        this.cell = cell;
    }


    // ############################# Functions #######################################

    /**
     * Creates an ArrayList of ExcelRowBeans by iterating through all sheets, rows and cells of a workbook
     *
     * @throws NullPointerException If the Workbook or the Sheet is not initialised
     */
    public void createRowList() throws NullPointerException {
        if (wb == null) {
            throw new NullPointerException("Can't create data fields from not initialised workbook!");
        }
        if (sheet == null) {
            throw new NullPointerException("Can't create data fields from not initialised sheet!");
        }

        for (Sheet sheet : wb) {
            for (Row row : sheet) {
                if (isRowNotEmpty(row)) {
                    fillCells(row);
                }
            }
        }
    }

    /**
     * Sets all the fields of an ExcelRowBeans object and adds it to the ArrayList
     *
     * @param row Row with cells to fill it into the fields of the ExcelRowBeans object
     */
    private void fillCells(Row row) {
        ExcelRowBeans beansRow = new ExcelRowBeans();
        beansRow.setID_Zeile(row.getCell(0));
        beansRow.set$Projektbezeichnung(row.getCell(1));
        beansRow.setZeilenbezeichnung(row.getCell(2));
        beansRow.setStart(row.getCell(3));
        beansRow.setProzent_Fertigstellung(row.getCell(4));
        beansRow.setDatum_Endfixierung(row.getCell(5));
        beansRow.setAbteilung(row.getCell(6));
        beansRow.setBemerkungen(row.getCell(7));
        this.rows.add(beansRow);
    }

    /**
     * Checks if the row is empty
     *
     * @param row That row that will be checked
     * @return boolean: True if the row is not empty; False if the row is empty
     */
    public boolean isRowNotEmpty(Row row) {
        for (Cell cell : row) {
            if (cell.getCellType() != CellType.BLANK) {
                return true;
            }
        }
        return false;
    }

    /**
     * Initialises the InputStream, Workbook, Sheet, Row and Cell of this class by
     * using the path and the
     * passed indices.
     *
     * @param sheetIndex Index of the sheet (0-based)
     * @param rowIndex   Index of the row (0-based)
     * @param cellIndex  Index of the cell (0-based)
     * @throws IOException If any of the called functions in the init process throws an
     *                     exception
     */
    public void init(int sheetIndex, int rowIndex, int cellIndex) throws IOException {
        createInputStream();
        createWorkbook();
        createSheet(sheetIndex);
        createRow(rowIndex);
        createCell(cellIndex);
        LOG.info("Auslesen erfolgreich");
    }


    /**
     * Creates an FileInputStream with the file that is defined by the abstract path
     *
     * @throws FileNotFoundException If the file is not found under the abstract path
     * @throws SecurityException     if a security manager exists and its checkRead method denies read access to the file
     */
    private void createInputStream() throws FileNotFoundException, SecurityException {
        input = new FileInputStream(path);
    }

    /**
     * Creates a workbook out of the InputStream
     *
     * @throws IOException                if an error occurs while reading the data
     * @throws EncryptedDocumentException If the Workbook given is password protected
     */
    private void createWorkbook() throws IOException, EncryptedDocumentException {
        wb = WorkbookFactory.create(input);
    }

    /**
     * Creates a sheet from the workbook at the passed index
     *
     * @param index Index of the sheet
     * @throws IllegalArgumentException if the index is out of range (index < 0 || index >= getNumberOfSheets()).
     */
    private void createSheet(int index) throws IllegalArgumentException {
        sheet = wb.getSheetAt(index);
    }

    /**
     * Creates a row from the sheet at the passed index
     *
     * @param index Index of the row
     * @throws IllegalArgumentException if the row at the passed index is null
     */
    private void createRow(int index) throws IllegalArgumentException {
        row = sheet.getRow(index);
        if (row == null) {
            throw new IllegalArgumentException("Array index out of bound!");
        }
    }

    /**
     * Creates a cell from the row at the passed index
     *
     * @param index Index of the cell
     * @throws IllegalArgumentException if the cell at the passed index is null
     */
    private void createCell(int index) throws IllegalArgumentException {
        cell = row.getCell(index);
        if (cell == null) {
            throw new IllegalArgumentException("Array index out of bound!");
        }
    }
}
