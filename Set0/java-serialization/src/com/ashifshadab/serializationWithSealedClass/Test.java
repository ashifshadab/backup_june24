package com.ashifshadab.serializationWithSealedClass;

import com.ashifshadab.serializationWithCollection.BookLibrary;
import com.ashifshadab.utils.PathConstant;
import com.ashifshadab.utils.ReadObjectFromFile;
import com.ashifshadab.utils.WriteObjectToFile;

public class Test {
    public static void main(String[] args) {
        Test test = new Test();
        test.case1();
    }

    private void case1() {
        System.out.println("Test Serializable Interface with Collection case:1");
        new WriteObjectToFile().persist(getHikerMan(), PathConstant.LOCAL_FILE_PATH + "HikerMan.ser");
        HikerMan hikerMan = (HikerMan) new ReadObjectFromFile().getObjectFromDisk(PathConstant.LOCAL_FILE_PATH + "HikerMan.ser");
        System.out.println(hikerMan);
    }

    private HikerMan getHikerMan(){
        return new HikerMan("XYX001","QWB12NOO989");
    }
}
