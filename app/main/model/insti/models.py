# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.main import db

Base = declarative_base()
metadata = Base.metadata


class CodeAge(db.Model):
    __tablename__ = 'code_age'
    __bind_key__ = "insti"

    age_no = db.Column(INTEGER(10), primary_key=True, nullable=False, comment='나이')
    gbn = db.Column(CHAR(1), primary_key=True, nullable=False, comment='구분. C=그룹. A=별칭')
    age_name = db.Column(String(64), primary_key=True, nullable=False, comment='나이 명칭')
    use_yn = db.Column(TINYINT(1), primary_key=True, nullable=False, server_default=text("'1'"), comment='사용여부')
    reg_date = db.Column(DateTime, primary_key=True, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='등록일시')


class CodeMast(db.Model):
    __tablename__ = 'code_mast'
    __bind_key__ = "insti"

    code_no = Column(INTEGER(10), primary_key=True)
    parent_code_no = Column(ForeignKey('code_mast.code_no'), nullable=False, index=True, comment='부모 코드')
    code_name = Column(String(64), nullable=False, comment='코드명')
    use_yn = Column(TINYINT(1), nullable=False, server_default=text("'1'"), comment='사용여부')
    depth = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    reg_id = Column(String(16), nullable=False, comment='등록자')
    reg_date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='등록일시')

    parent = relationship('CodeMast', remote_side=[code_no])


class Insti(db.Model):
    __tablename__ = 'insti'
    __bind_key__ = "insti"

    insti_no = db.Column(db.Integer, primary_key=True)
    insti_id = db.Column(db.String(32), nullable=False, index=True)
    insti_name = db.Column(db.String(128), nullable=False, index=True)
    insti_kname = db.Column(db.String(16))
    insti_type1 = db.Column(db.SmallInteger, nullable=False)
    insti_type2 = db.Column(db.SmallInteger)
    category1 = db.Column(db.SmallInteger, nullable=False)
    category2 = db.Column(db.SmallInteger)
    category3 = db.Column(db.SmallInteger)
    area1 = db.Column(db.SmallInteger, nullable=False)
    area2 = db.Column(db.SmallInteger, nullable=False)
    area3 = db.Column(db.SmallInteger)
    address1 = db.Column(db.String(128), nullable=False)
    address2 = db.Column(db.String(128))
    address3 = db.Column(db.String(128))
    building = db.Column(db.String(128))
    zipcode = db.Column(db.String(8))
    old_address = db.Column(db.String(128))
    old_zipcode = db.Column(db.String(8))
    latitude = db.Column(db.String(32))
    longitude = db.Column(db.String(32))
    insti_img = db.Column(db.String(128))
    founder = db.Column(db.String(64))
    num_teacher = db.Column(db.SmallInteger)
    score = db.Column(db.Integer)
    upd_date = db.Column(db.DateTime)
    upd_id = db.Column(db.String(16))
    confirm_yn = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    confirm_date = db.Column(db.DateTime)
    use_yn = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


class InstiAddres(db.Model):
    __tablename__ = 'insti_address'
    __bind_key__ = "insti"

    insti_no = Column(INTEGER(11), primary_key=True)
    latitude = Column(String(32))
    longitude = Column(String(32))
    building = Column(String(128), nullable=False)
    dong = Column(String(128), nullable=False)
    old_address = Column(String(128), nullable=False)
    new_zip = Column(String(8), nullable=False)
    old_zip = Column(String(8), nullable=False)


class Place(db.Model):
    __tablename__ = 'place'
    __bind_key__ = "insti"

    place_no = Column(INTEGER(10), primary_key=True, comment='위치 식별자')
    gbn_no = Column(INTEGER(10), nullable=False, comment='장소 구분자')
    place_name = Column(String(128), nullable=False, comment='장소명')
    kakao_place_id = Column(String(128), comment='카카오 지도 장소 아이디')
    kakao_place_url = Column(String(128), comment='카카오 지도 장소 URL')
    latitude = Column(String(32), nullable=False, comment='위도')
    longitude = Column(String(32), nullable=False, comment='경도')
    tel = Column(String(32), nullable=False, comment='전화번호')
    address = Column(String(128), nullable=False, comment='주소')
    use_yn = Column(TINYINT(1), nullable=False, server_default=text("'1'"), comment='사용여부(1=사용)')
    reg_date = Column(DateTime, nullable=False, comment='등록일시')
    upd_date = Column(DateTime, comment='마지막 수정일시')


class InstiAddition(db.Model):
    __tablename__ = 'insti_addition'
    __bind_key__ = "insti"

    insti_no = Column(ForeignKey('insti.insti_no'), primary_key=True, nullable=False)
    item_name = Column(CHAR(2), primary_key=True, nullable=False)
    seq = Column(TINYINT(4), nullable=False)
    item_value = Column(String(128), primary_key=True, nullable=False)
    item_property = Column(String(128))
    use_yn = Column(TINYINT(1), server_default=text("'1'"))

    insti = relationship('Insti')


class InstiCharge(db.Model):
    __tablename__ = 'insti_charge'
    __bind_key__ = "insti"

    insti_no = Column(ForeignKey('insti.insti_no'), primary_key=True, nullable=False)
    subject = Column(String(128), primary_key=True, nullable=False)
    num_limit = Column(INTEGER(11), primary_key=True, nullable=False)
    period = Column(String(12), primary_key=True, nullable=False)
    tech_hour = Column(INTEGER(11), primary_key=True, nullable=False)
    charge1 = Column(INTEGER(11), primary_key=True, nullable=False)
    charge2 = Column(INTEGER(11))
    charge3 = Column(INTEGER(11))
    charge4 = Column(INTEGER(11))
    charge5 = Column(INTEGER(11))
    charge6 = Column(INTEGER(11))
    charge7 = Column(INTEGER(11))
    extra_charge = Column(INTEGER(11))
    total_charge = Column(INTEGER(11), primary_key=True, nullable=False)

    insti = relationship('Insti')


class InstiDetail(db.Model):
    __tablename__ = 'insti_detail'
    __bind_key__ = "insti"

    insti_no = Column(ForeignKey('insti.insti_no'), primary_key=True, nullable=False, comment='학원번호')
    gbn = Column(CHAR(2), primary_key=True, nullable=False, comment='구분. DS:세부과목, AG:대상나이')
    code_no = Column(INTEGER(10), primary_key=True, nullable=False, comment='코드값')
    use_yn = Column(TINYINT(1), nullable=False, server_default=text("'1'"), comment='사용여부')

    insti = relationship('Insti')


class InstiTogether(db.Model):
    __tablename__ = 'insti_together'
    __bind_key__ = "insti"

    insti_no = Column(ForeignKey('insti.insti_no'), primary_key=True, nullable=False)
    target_insti_no = Column(ForeignKey('insti.insti_no'), primary_key=True, nullable=False, index=True)
    rnk = Column(SMALLINT(6), nullable=False)

    insti = relationship('Insti', primaryjoin='InstiTogether.insti_no == Insti.insti_no')
    insti1 = relationship('Insti', primaryjoin='InstiTogether.target_insti_no == Insti.insti_no')
