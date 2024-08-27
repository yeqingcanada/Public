from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.authentication_context import AuthenticationContext
import pandas as pd

# 配置参数
site_url = 'https://collab.lilly.com/sites/ManufacturingWarehouseCapacityProject/'
username = 'ye@miebach.com'
password = 'CrCo2!14AQ'
library_name = 'Documents'

# 认证并连接到SharePoint
ctx_auth = AuthenticationContext(site_url)
if ctx_auth.acquire_token_for_user(username, password):
    ctx = ClientContext(site_url, ctx_auth)
    web = ctx.web
    ctx.load(web)
    ctx.execute_query()

    print("Authenticated into SharePoint site: {0}".format(web.properties['Title']))

    # 获取文档库中的文件
    library = ctx.web.lists.get_by_title(library_name)
    files = library.root_folder.files
    ctx.load(files)
    ctx.execute_query()

    file_list = []
    for file in files:
        file_list.append({"Name": file.properties["Name"], "ServerRelativeUrl": file.properties["ServerRelativeUrl"]})
    
    df = pd.DataFrame(file_list)
    print(df)
else:
    print(ctx_auth.get_last_error())
