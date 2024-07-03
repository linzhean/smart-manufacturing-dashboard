package tw.edu.ntub.imd.birc.sodd.service;

import tw.edu.ntub.imd.birc.sodd.bean.UserAccountBean;

import java.util.List;

public interface UserAccountService extends BaseService<UserAccountBean, String> {
    List<UserAccountBean> searchByUserValue(String departmentId, String name, String identity, Integer nowPage);

    Integer countUserList(String departmentId, String identity, String name);
}
