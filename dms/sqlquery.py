#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Chris
@license: Apache Licence
@file: sqlquery.py
@time: 8/3/16 2:44 PM
"""

RFT_CAV = '''
select
    T1.dbid 'db_id',
    T1.id 'dms_id',
    T1.title 'title',
    T3.name 'project',
    T4.name 'sw_version',
    T2.fullname 'submitter',
    T1.submit_date 'submit_date',
    T5.name 'found_in_product',
    T1.implemented_status 'implemented_status'
from DMS_dbo.issue T1,DMS_dbo.project T3,DMS_dbo.sw_label T4,DMS_dbo.users T2,DMS_dbo.statedef T5,DMS_dbo.external_supplier T7
where T1.found_in_product = T3.dbid and
    T1.sw_version = T4.dbid and
    T1.submitter = T2.dbid and
    T1.state = T5.id and
    T1.externalsupplier = T7.dbid and
    (T1.dbid <> 0 and
    ((T1.implemented_status like '%ready for test%' and
    (T1.found_during = 'Customer Application Verification' or T1.found_during = 'CAV')))) and
    (((T7.dbid in (select parent_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16778755 and child_dbid in (select child_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16777308 and parent_dbid = 79773266)))))
    order by T1.submit_date ASC
'''

QUALIFY_CAV = '''
select distinct
    T1.dbid,
    T1.id,
    T1.title,
    T1.abc_rank,
    T3.name,
    T4.name,
    T1.submit_date,
    T2.fullname
from DMS_dbo.issue T1,DMS_dbo.statedef T3,DMS_dbo.project T4,DMS_dbo.users T2,DMS_dbo.external_supplier T6
where T1.state = T3.id and
    T1.found_in_product = T4.dbid and
    T1.submitter = T2.dbid and
    T1.externalsupplier = T6.dbid and
    (T1.dbid <> 0 and ((T3.name = 'Qualifying' and
    (T1.found_during = 'Customer Application Verification' or T1.found_during = 'CAV')))) and
    (((T6.dbid in (select parent_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16778755 and child_dbid in (select child_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16777308 and parent_dbid = 79773266)))))
order by T1.submit_date ASC
'''

RFT_LV = '''
select distinct
    T1.dbid,
    T1.id,
    T4.name,
    T1.title,
    T3.name,
    T1.submit_date,
    T2.login_name,
    T51.verified_in
from ( ( ( ( ( ( DMS_dbo.issue T1 INNER JOIN DMS_dbo.project T4 ON T1.found_in_product = T4.dbid ) INNER JOIN DMS_dbo.statedef T3 ON T1.state = T3.id ) INNER JOIN DMS_dbo.users T2 ON T1.submitter = T2.dbid ) INNER JOIN DMS_dbo.external_supplier T6 ON T1.externalsupplier = T6.dbid ) LEFT OUTER JOIN DMS_dbo.parent_child_links T51mm ON T1.dbid = T51mm.parent_dbid  and 16785462 = T51mm.parent_fielddef_id  ) LEFT OUTER JOIN DMS_dbo.deliveryrecord T51 ON T51mm.child_dbid = T51.dbid  )
where T1.dbid <> 0 and ((T51.verified_in is NULL and (T3.name in ('Assigned','Integrated','Investigating','Submitted','Verified')) and (T51.delivered_in is not NULL and (T51.delivered_in not like '%Invalid Record%' or T51.delivered_in is NULL) and (T51.delivered_in not like '%Will not Deliver%' or T51.delivered_in is NULL) and T51.decisionstatus like '%Accept%') and (T1.found_during = 'LV' or T1.found_during = 'Localization Verification'))) and
    (((T6.dbid in (select parent_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16778755 and child_dbid in (select child_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16777308 and parent_dbid = 79773266)))))
order by T1.submit_date DESC
'''

QUALIFY_LV = '''
select distinct
    T1.dbid,
    T1.id,
    T1.title,
    T3.name,
    T2.fullname,
    T1.submit_date
from DMS_dbo.issue T1,DMS_dbo.statedef T3,DMS_dbo.users T2,DMS_dbo.external_supplier T6
where T1.state = T3.id and T1.submitter = T2.dbid and T1.externalsupplier = T6.dbid and (T1.dbid <> 0 and ((T3.name = 'Qualifying' and (T1.found_during = 'LV' or T1.found_during = 'Localization Verification')))) and  (
((T6.dbid in (select parent_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16778755 and child_dbid in (select child_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16777308 and parent_dbid = 79773266))))) order by T1.submit_date DESC
'''

LR_LV = '''
select distinct
    T1.dbid,
    T1.lr_id,
    T2.id,
    T2.title,
    T1.responsible_organization,
    T1.assign_to_distribution,
    T1.assign_to_sub_distribu,T5.name,T6.name,
    T1.created_date,T4.name,
    T1.leakage_type,T7.name
from DMS_dbo.leakagerecord T1,DMS_dbo.issue T2,DMS_dbo.project T5,DMS_dbo.statedef T6,DMS_dbo.ca T3,DMS_dbo.ca_customergroup T4,DMS_dbo.ratl_replicas T7,DMS_dbo.external_supplier T8,DMS_dbo.external_supplier T9,DMS_dbo.external_supplier T10
where T1.generating_record = T2.dbid and
    T2.found_in_product = T5.dbid and
    T2.externalsupplier = T9.dbid and
    T1.state = T6.id and
    T1.ca_record = T3.dbid and
    T3.group_region = T4.dbid and
    T3.externalsupplier = T10.dbid and
    T1.ratl_mastership = T7.dbid and
    T1.externalsupplier = T8.dbid and
    (T1.dbid <> 0 and ((T1.assign_to_sub_distribu = 'DL-WW-IL-ODM-OMV-LV' or (T1.lr_type = 'External' and T1.assign_to_sub_distribu = 'DL-WW-IL-Android-PD-SW-PSV-LV') or T1.assign_to_sub_distribu = 'DL-WW-IL-OMV-Localization Verification'))) and  (
((T8.dbid in (select parent_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16778755 and child_dbid in (select child_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16777308 and parent_dbid = 79773266))))
 AND ((T9.dbid = 0 or T9.dbid is NULL or T9.dbid in (select parent_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16778755 and child_dbid in (select child_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16777308 and parent_dbid = 79773266))))
 AND ((T10.dbid = 0 or T10.dbid is NULL or T10.dbid in (select parent_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16778755 and child_dbid in (select child_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16777308 and parent_dbid = 79773266)))))
'''