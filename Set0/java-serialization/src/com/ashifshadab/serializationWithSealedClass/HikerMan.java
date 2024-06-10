package com.ashifshadab.serializationWithSealedClass;

public final class HikerMan extends Human{
    private final String hikerMenId;

    public HikerMan(String hikerMenId) {
        this.hikerMenId = hikerMenId;
    }

    public HikerMan(String humanName, String hikerMenId) {
        super(humanName);
        this.hikerMenId = hikerMenId;
    }


    @Override
    public String toString() {
        return super.toString()+"HikerMan{" +
                "hikerMenId='" + hikerMenId + '\'' +
                '}';
    }
}
