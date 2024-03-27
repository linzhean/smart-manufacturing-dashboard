package tw.edu.ntub.imd.birc.sodd.exception;

import tw.edu.ntub.birc.common.exception.ProjectException;

public class DuplicateCreateException extends ProjectException {
    public DuplicateCreateException(String message) {
        super(message);
    }

    @Override
    public String getErrorCode() {
        return "Create - Duplicate";
    }
}
