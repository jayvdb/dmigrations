from gcap.apps.dmigrations import migrations as m

migration = m.Migration(sql_up="INSERT INTO mock VALUES (9, 2)", sql_down="")
