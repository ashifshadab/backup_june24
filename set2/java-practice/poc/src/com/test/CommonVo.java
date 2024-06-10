package com.test;

import java.util.Map;
public abstract class CommonVo {
    /**
     * Used for object validation for required field
     * @return boolean
     */
    public abstract boolean isValidObject();

    public abstract Map<String, Object> getData();

    public abstract String getStatus();
    public abstract void setStatus(String status);
}
