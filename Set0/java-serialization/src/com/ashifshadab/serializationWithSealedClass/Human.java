package com.ashifshadab.serializationWithSealedClass;

import java.io.Serial;
import java.io.Serializable;

sealed public class Human implements Serializable permits HandyMan,HikerMan {
    @Serial
    private static final long serialVersionUID = 1L;
    private String HumanName;

    public Human() {
    }

    public Human(String humanName) {
        HumanName = humanName;
    }

    public String getHumanName() {
        return HumanName;
    }

    public void setHumanName(String humanName) {
        HumanName = humanName;
    }

    @Override
    public String toString() {
        return "Human{" +
                "HumanName='" + HumanName + '\'' +
                '}';
    }
}
