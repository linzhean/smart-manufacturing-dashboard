package tw.edu.ntub.imd.birc.sodd.service.impl;

import org.springframework.transaction.annotation.Transactional;
import tw.edu.ntub.imd.birc.sodd.databaseconfig.dao.BaseDAO;
import tw.edu.ntub.imd.birc.sodd.exception.NotFoundException;
import tw.edu.ntub.imd.birc.sodd.service.BaseService;
import tw.edu.ntub.imd.birc.sodd.service.transformer.BeanEntityTransformer;
import tw.edu.ntub.birc.common.util.JavaBeanUtils;

import java.io.Serializable;
import java.util.Optional;

public abstract class BaseServiceImpl<B, E, ID extends Serializable> extends BaseViewServiceImpl<B, E, ID> implements BaseService<B, ID> {
    private final BaseDAO<E, ID> baseDAO;

    public BaseServiceImpl(BaseDAO<E, ID> d, BeanEntityTransformer<B, E> transformer) {
        super(d, transformer);
        this.baseDAO = d;
    }

    @Transactional
    @Override
    public void update(ID id, B b) {
        Optional<E> optional = baseDAO.findById(id);
        if (optional.isPresent()) {
            E entity = optional.get();
            JavaBeanUtils.copy(b, entity);
            baseDAO.update(entity);
        } else {
            throw new NotFoundException("找不到資料, id = " + id);
        }
    }

    @Transactional
    @Override
    public void delete(ID id) {
        baseDAO.deleteById(id);
    }
}
