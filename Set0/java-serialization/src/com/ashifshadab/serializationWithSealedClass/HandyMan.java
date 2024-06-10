package com.ashifshadab.serializationWithSealedClass;

public final class HandyMan extends Human{
    private final String HandyManId;

    public HandyMan(String handyManId) {
        HandyManId = handyManId;
    }

    public HandyMan(String humanName, String handyManId) {
        super(humanName);
        HandyManId = handyManId;
    }

    @Override
    public String toString() {
        return super.toString()+"HandyMan{" +
                "HandyManId='" + HandyManId + '\'' +
                '}';
    }
}
