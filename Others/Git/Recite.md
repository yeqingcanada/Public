| command                                                                         | descritpion                                                                                                                  |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| git status                                                                      | 目前 checking all the status of both working directory and staging area                                                      |
| Git diff                                                                        | 目前 Working directory 中的@@变化                                                                                            |
| Git diff --staged                                                               | 目前 stage 中的@@变化                                                                                                        |
| git diff HEAD~2 HEAD file.txt                                                   | 比较中间有相隔的两次 commit 的之间的某个文件                                                                                 |
|                                                                                 |                                                                                                                              |
| git log --oneline                                                               | 所有 commit Summary                                                                                                          |
| git log --stat                                                                  | 所有 commit，发生改变的文件                                                                                                  |
| git log --oneline --stat                                                        | 所有 commit，类似 above，文件，short 版本                                                                                    |
| git log --patch                                                                 | 所有 commit @@                                                                                                               |
|                                                                                 |                                                                                                                              |
| git log file.txt                                                                | # Shows the commits that touched file.txt                                                                                    |
| git log --stat file.txt                                                         | # Shows statistics (the number of changes) for file.txt                                                                      |
| git log --patch file.txt                                                        | # Shows the patches (changes) applied to file.txt                                                                            |
|                                                                                 |                                                                                                                              |
| Git show head~1                                                                 | 某次 commit 的@@变化                                                                                                         |
| Git show head~1:file.js                                                         | 某次 commit 后，file 文件每行具体内容                                                                                        |
|                                                                                 |                                                                                                                              |
| git restore --staged file.js                                                    | 从 staged area 到 working directory                                                                                          |
| git restore file.js                                                             | 在 working directory 中 file.js 变成没改以前的样子                                                                           |
| git restore --source=HEAD~2 file.js                                             | 将特定 commit 的特定 file，恢复到 working directory                                                                          |
| 如果想恢复某次 commit 删掉的文件，找到它上次一 commit，利用这个命令可以将其回复 |                                                                                                                              |
|                                                                                 |                                                                                                                              |
| Git checkout                                                                    | 去到某一个 commit/branch                                                                                                     |
|                                                                                 |                                                                                                                              |
| BRANCHING                                                                       |                                                                                                                              |
| 在 bugfix branch 上：                                                           |                                                                                                                              |
| Gti diff master = git diff master..bugfix                                       | 对比两个 branch 的具体不同之处，bugfix 在以 master 为基础的情况下，改变了哪些                                                |
| Gti diff master --name-status                                                   |                                                                                                                              |
| Git log master                                                                  | 不是对比，是单纯的相当于 master 的 git log                                                                                   |
| Git show master                                                                 | 单纯的相当于 master 的 git show，git show 不带任何参数，会 show 最后一次的 commit 的变化                                     |
|                                                                                 |                                                                                                                              |
| Switch branch 之前，还有没 commit 的内容，利用 stash                            |                                                                                                                              |
| git stash push -am 'my new stash'                                               |                                                                                                                              |
| git stash list                                                                  |                                                                                                                              |
| git stash show 0                                                                |                                                                                                                              |
| git stash apply 0                                                               |                                                                                                                              |
| git stash drop 0                                                                |                                                                                                                              |
|                                                                                 |                                                                                                                              |
| Git merge bugfix                                                                | 出现 conflix 后，可以直接去 conflict 所在文件，改为需要的内容，甚至可以两种都不用，重现一下。再 commit，这次 commit 就会成功 |
| git log --oneline --all --graph                                                 |                                                                                                                              |
|                                                                                 |                                                                                                                              |
| 去掉一次 commit                                                                 |                                                                                                                              |
| Git reset --hard head~1                                                         | 回到 head 往前一次的 commit，只能本地执行                                                                                    |
| git reset 'HEAD@{1}'                                                            | Undo Git reset --hard head~1                                                                                                 |
| Git revert -m 1 head                                                            | 1 指的是 master branch，会新生成一个 commit，把 head 这次 commit 的操作，进行反向操作                                        |

| ffbf7a5 | 添加 file1，file2   |
| ------- | ------------------- |
| c48b678 | File1，2 分别减一行 |
| 25e717e | 添加 file2.js       |
| b84c3bf | File1 加三行        |
| 3f73f85 | 删除 file2.js       |
| e8137bc | 添加 file3          |

git push github master(local-branch):code_review(remote-branch)

git config core.ignorecase false  
git rm -r --cached .  
git add .  
git commit -m "Clearing git cache"  
git push azure master --force
