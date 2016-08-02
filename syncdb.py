import pymssql

server = 'SELDSQL975\\PRD5'
db_name = 'DMS_copy'
user = 'omvteam_read'
password = 'Tr54Ewd654Hg!'

sql_query = '''
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
         (((T7.dbid in (select parent_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16778755 and child_dbid in (select child_dbid from DMS_dbo.parent_child_links where parent_fielddef_id = 16777308 and parent_dbid = 79773266))))) order by T1.submit_date ASC
'''

try:
    conn = pymssql.connect(server, user, password, db_name)
    cursor = conn.cursor()
    cursor.execute(sql_query)
except pymssql.Error, e:
    print e

for row in cursor:
    print('row = %r' % (row,))
