package tw.edu.ntub.imd.birc.sodd.exception.file;

public class UnauthorizedException extends FileException {

    public UnauthorizedException(Throwable cause) {
        super("檔案權限不足", cause);
    }

    @Override
    public String getReason() {
        return "Unauthorized";
    }
}
