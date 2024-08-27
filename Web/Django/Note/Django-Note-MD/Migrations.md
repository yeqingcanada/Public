1. 将一个已有的 string field 改成外键
   1. 删除已有 string field，python manage.py makemigrations + python manage.py migrate（需要先进行这个 migrate，不能自动将 string 变成 bigint）
   2. 添加外键，再进行第二次 python manage.py makemigrations + python manage.py migrate
2. 将一个已有一对一主键，改成一对多外键。例子：change project manager timestamp，原本是一对一连 project master，但是同一个 project 应该有多个 change timestamp
   1. 不能直接改，因为无法 migrate，有冲突
   2. 步骤：
      1. 将已经存在的 table 在 SQL 层面删除
      2. 删除 [dbo].[django_migrations] 表中的最后一次 migration（就是新建这个 table 的那次 migrate）
      3. 重新 python manage.py makemigrations + python manage.py migrate
