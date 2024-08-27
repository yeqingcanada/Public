{
  /*
    之所以弃用这段：app 入口需要check isActiveToken，每个private route都需要一次post，有些浪费。其次，用到isActiveToken这个方法的位置，都需要异步函数作为外罩private route component需要变成async的
    isActiveToken： 1，是否存在，2，是否过期，3，没过期，是否有效。最后一个情况只存在于local，因为多个app共享host端口
    多次刷新：是因为isActiveToken()方法中包含这句window.location = "/login"，这句会刷新整个app，会去到app useEffect，会再次访问isActiveToken()，只需要去掉这句即可，因为private route中<Redirect to="/login" />会跳转，并且不会刷新app
    */
}
async function _isActiveToken() {
  if (!_.isEmpty(getJwt())) {
    console.log("test 1");
    try {
      const token = { [tokenKey]: getJwt() };
      const { data: message } = await http.post(verifyTokenAPI, token);
      return true;
    } catch (error) {
      if (error.response.status == 401 || error.response.status == 400) {
        logout();
        console.log("error.response.data.detail", error.response.data.detail);
        return false;
      }
    }
  } else {
    console.log("test 2");
    return false;
  }
}

export const verifyTokenAPI = "/auth/jwt/verify/";

{
  /*
   ******************************************** 2023-02-14 **************************************************
   */
}

// set the prevPath in the state

<Link
  to={{
    pathname: customContent.toPath(row),
    state: { prevPath: customContent.pathName || null },
  }}
  onClick={handleClearFilter}
></Link>;

const columns = [
  {
    path: "alter_title",
    label: "Alternative Title",
    customContent: {
      type: "link",
      toPath: (data) =>
        alternativeDetailRouter(
          data.project_id,
          data.project_title,
          data.alter_id,
          data.alter_title
        ),
      pathName: history.location.pathname,
    },
  },
];

// get the prevPath in the state

const history = useHistory();
const previousPath = history.location.state
  ? history.location.state.prevPath
  : "";
