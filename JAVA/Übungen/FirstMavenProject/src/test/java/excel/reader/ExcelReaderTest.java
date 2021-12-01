package excel.reader;

import org.junit.Test;

import static org.junit.Assert.*;

public class ExcelReaderTest {
    ExcelReader reader = new ExcelReader("C:\\Users\\toplitsc\\Downloads\\7000_MPM_Milestones_Eng_Dev.xls");
        @Test
        public void readTest(){
            reader.readFile(0,2,7);
            System.out.println(reader.getCell().toString());
        }
}