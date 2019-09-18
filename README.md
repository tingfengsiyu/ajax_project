# ajax_project 
使用ajax +bootstrap实现学生选课系统，增删查改等
编辑时，使用给表格绑定id，自定义属性，获取其id自定义属性

ajax发送数据时
data中的v只是字符串或数字正常发送
data中的v包含数组添加tradition:true 才可以传递过去；
默认包含字典发送不过去，传递字典使用data:{"k1":JSON.stringify({})}，后台拿到数据

