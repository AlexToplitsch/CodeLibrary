package excel.comparator;

import excel.beans.row.ExcelRowBeans;
import org.apache.poi.ss.usermodel.Cell;

import java.util.Comparator;
import java.util.Locale;

public class ExcelComparator implements Comparator<ExcelRowBeans> {
    private final int cellIndex;
    private final boolean desc;
    public ExcelComparator(int cellIndex, boolean desc){
        this.cellIndex = cellIndex;
        this.desc = desc;
    }
    @Override
    public int compare(ExcelRowBeans o1, ExcelRowBeans o2) {
        Cell c1 = getCell(o1);
        Cell c2 = getCell(o2);
        if(c1 == null && c2 == null) {
            return 0;
        }else if(c1 == null){
            return 1;
        }else if(c2 == null) {
            return -1;
        }
        int res =  c1.toString().toLowerCase(Locale.ROOT).compareTo(c2.toString().toLowerCase(Locale.ROOT));
        if(desc){
            res = res * -1;
        }
        return res;
    }

    /**
     * @param o The instance of the ExcelRowBeans class
     * @return A field from the object o
     */
    private Cell getCell(ExcelRowBeans o) {
        switch(cellIndex){
            case 0:
                return o.getID_Zeile();
            case 1:
                return o.get$Projektbezeichnung();
            case 2:
                return o.getZeilenbezeichnung();
            case 3:
                return o.getStart();
            case 4:
                return o.getProzent_Fertigstellung();
            case 5:
                return o.getDatum_Endfixierung();
            case 6:
                return o.getAbteilung();
            case 7:
                return o.getBemerkungen();
        }
        throw new IllegalArgumentException("No valid cell index!");
    }
}
