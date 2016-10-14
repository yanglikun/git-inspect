__author__='yanglikun'
columns=' id, plu, sku_id, sku_amount,ticket_type_person,created, modified, yn'
fields='id,plu,skuId,skuAmount,ticketTypePerson,created,modified,yn'

columnArr=columns.split(",")
fieldsArr=fields.split(",")
for a,b in zip(columnArr,fieldsArr):
    print('<result column="'+a+'"  property="'+b+'"/>')