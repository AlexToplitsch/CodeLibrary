package excel.comparator;

import excel.beans.row.ExcelRowBeans;
import org.apache.poi.ss.usermodel.Cell;

import java.util.Comparator;

public class ExcelComparator implements Comparator<Cell> {
    @Override
    public int compare(Cell o1, Cell o2) {
        return 0;
    }
}
