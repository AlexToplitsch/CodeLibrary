package com.company;
import menu.ExcelMenu;
import menu.filechooser.MyFileChooser;
import org.apache.poi.hssf.extractor.ExcelExtractor;
import menu.SortingMenu;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.poifs.filesystem.POIFSFileSystem;
import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        new ExcelMenu();
    }
}
