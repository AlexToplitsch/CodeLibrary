package excel.beans.row;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.poi.ss.format.CellDateFormatter;
import org.apache.poi.ss.usermodel.Cell;

import java.io.Serializable;
import java.util.ArrayList;
import java.sql.Date;
import java.util.Objects;

public class ExcelRowBeans implements Serializable {
    // ######################## Properties ###########################################
    private Logger log = LogManager.getLogger(ExcelRowBeans.class);

    private Cell ID_Zeile;
    private Cell $Projektbezeichnung;
    private Cell Zeilenbezeichnung;
    private Cell Start;
    private Cell Prozent_Fertigstellung;
    private Cell Datum_Endfixierung;
    private Cell Abteilung;
    private Cell Bemerkungen;

    // ######################## Constructor ##########################################
    public ExcelRowBeans() {

    }

    // ######################## Getter/Setter #########################################

    public Cell getID_Zeile() {
        return ID_Zeile;
    }

    public void setID_Zeile(Cell ID_Zeile) {
        this.ID_Zeile = ID_Zeile;
    }

    public Cell get$Projektbezeichnung() {
        return $Projektbezeichnung;
    }

    public void set$Projektbezeichnung(Cell $Projektbezeichnung) {
        if ($Projektbezeichnung != null) {
            $Projektbezeichnung.setCellValue($Projektbezeichnung.toString().
                    replaceAll("'", "''"));
        }
        this.$Projektbezeichnung = $Projektbezeichnung;
    }

    public Cell getZeilenbezeichnung() {
        return Zeilenbezeichnung;
    }

    public void setZeilenbezeichnung(Cell zeilenbezeichnung) {
        if (zeilenbezeichnung != null) {
            zeilenbezeichnung.setCellValue(zeilenbezeichnung.toString().
                    replaceAll("'", "''"));
        }
        Zeilenbezeichnung = zeilenbezeichnung;
    }

    public Cell getStart() {
        return Start;
    }

    public void setStart(Cell start) {
        if (start != null) {
            CellDateFormatter formatter = new CellDateFormatter("yyyy-MM-dd");
            try {
                Date date = new Date(start.getDateCellValue().getTime());
                start.setCellValue(date);
            } catch (Exception e) {
                log.warn(e.getMessage());
                start.setCellValue(new Date(0,0,0));
            }
        }
        Start = start;
    }

    public Cell getProzent_Fertigstellung() {
        return Prozent_Fertigstellung;
    }

    public void setProzent_Fertigstellung(Cell prozent_Fertigstellung) {
        Prozent_Fertigstellung = prozent_Fertigstellung;
    }

    public Cell getDatum_Endfixierung() {
        return Datum_Endfixierung;
    }

    public void setDatum_Endfixierung(Cell datum_Endfixierung) {
        if (datum_Endfixierung != null) {
            CellDateFormatter formatter = new CellDateFormatter("yyyy-MM-dd");
            try {
                Date date = new Date(datum_Endfixierung.getDateCellValue().getTime());
                datum_Endfixierung.setCellValue(date);
            } catch (Exception e) {
                log.warn(e.getMessage());
            }
            Datum_Endfixierung = datum_Endfixierung;
        }
    }

    public Cell getAbteilung() {

        return Abteilung;
    }

    public void setAbteilung(Cell abteilung) {
        if (abteilung != null) {
            abteilung.setCellValue(abteilung.toString().
                    replaceAll("'", "''"));
        }
        Abteilung = abteilung;
    }

    public Cell getBemerkungen() {
        return Bemerkungen;
    }

    public void setBemerkungen(Cell bemerkungen) {
        if (bemerkungen != null) {
            bemerkungen.setCellValue(bemerkungen.toString().
                    replaceAll("'", "''"));
        }
        Bemerkungen = bemerkungen;
    }


    // ######################## Functions  ###########################################

    /**
     * Sets all the fields of this class from the passed ArrayList
     *
     * @param cells List of cells, that are written in the excel
     */
    public void setFields(ArrayList<Cell> cells) {
        ID_Zeile = cells.get(0);
        $Projektbezeichnung = cells.get(1);
        Zeilenbezeichnung = cells.get(2);
        Start = cells.get(3);
        Prozent_Fertigstellung = cells.get(4);
        Datum_Endfixierung = cells.get(5);
        Abteilung = cells.get(6);
        Bemerkungen = cells.get(7);
    }

    /**
     * @return All fields from this class as ArrayList fo cells
     */
    public ArrayList<Cell> toArrayList() {
        ArrayList<Cell> cells = new ArrayList<Cell>();
        cells.add(getID_Zeile());
        cells.add(get$Projektbezeichnung());
        cells.add(getZeilenbezeichnung());
        cells.add(getStart());
        cells.add(getProzent_Fertigstellung());
        cells.add(getDatum_Endfixierung());
        cells.add(getAbteilung());
        cells.add(getBemerkungen());
        return cells;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        ExcelRowBeans that = (ExcelRowBeans) o;
        return Objects.equals(ID_Zeile, that.ID_Zeile) && Objects.equals($Projektbezeichnung, that.$Projektbezeichnung) &&
                Objects.equals(Zeilenbezeichnung, that.Zeilenbezeichnung) &&
                Objects.equals(Start, that.Start) && Objects.equals(Prozent_Fertigstellung, that.Prozent_Fertigstellung) && Objects.equals
                (Datum_Endfixierung,
                        that.Datum_Endfixierung) && Objects.equals(Abteilung, that.Abteilung) && Objects.equals(Bemerkungen,
                that.Bemerkungen);
    }

    @Override
    public int hashCode() {
        return Objects.hash(ID_Zeile, $Projektbezeichnung, Zeilenbezeichnung, Start, Prozent_Fertigstellung, Datum_Endfixierung,
                Abteilung, Bemerkungen);
    }
}
