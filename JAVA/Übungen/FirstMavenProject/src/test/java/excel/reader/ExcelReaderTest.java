package excel.reader;

import excel.beans.row.ExcelRowBeans;
import org.junit.Test;

import java.io.IOException;
import java.util.ArrayList;


public class ExcelReaderTest {
    ExcelReader reader = new ExcelReader("C:\\Users\\toplitsc\\Downloads\\7000_MPM_Milestones_Eng_Dev.xls");
        @Test
        public void readTest(){
            try {
                reader.init(0, 2, 7);
                reader.createRowList();
                ArrayList<ExcelRowBeans> rows = reader.rows;
            }catch(IOException e){
                System.out.println(e.getMessage());
            }
            System.out.println(reader.getCell().toString());
        }
}