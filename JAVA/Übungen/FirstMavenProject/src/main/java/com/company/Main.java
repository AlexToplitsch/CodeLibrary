package com.company;
import org.apache.poi.hssf.extractor.ExcelExtractor;
import menu.SortingMenu;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.poifs.filesystem.POIFSFileSystem;
import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try {
            POIFSFileSystem fileSystem = new POIFSFileSystem(new File("C:\\Users\\toplitsc\\Downloads\\7000_MPM_Milestones_Eng_Dev.xls"));
            HSSFWorkbook workbook = new HSSFWorkbook(fileSystem);
            ExcelExtractor extractor = new ExcelExtractor(workbook);
            System.out.println(extractor.getDocument());
        } catch (IOException e) {
            e.printStackTrace();
        }
        new SortingMenu();
    }
}
