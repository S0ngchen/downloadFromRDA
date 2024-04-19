## DOWNLOAD DATAS FROM UCRA
## 从UCRA下载数据的脚本
When downloading data from rda.ucar.edu., the download script will be always stoped downloading due to various reasons. This script ensure continuous and efficient downloading of data. It can automatically resubmit the download request when access is denied and download automaticly.

The downloading script: rda-download.py is also provided. modifying the commented content to download automaticly.

由于下载rda.ucar.edu.的数据时，其提供的下载脚本总是会因为各种原因被拒绝访问而停止下载。为了保证连续且高效的下载数据，而编写了这个脚本。这个脚本可以实现在被拒绝访问后自动再次提交下载请求，实现完全自动化的下载。

本脚本带了一个改进后的下载脚本：rda-download.py，通过修改其中被注释处的内容可以实现自动下载。