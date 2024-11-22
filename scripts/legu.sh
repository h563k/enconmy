#!/bin/bash

# 指定项目目录
PROJECT_DIR="/opt/economy"

# 指定Python脚本及其主函数
PYTHON_SCRIPT="$PROJECT_DIR/works/legu.py"
MAIN_FUNCTION="legu_main"

# 进入项目目录
cd "$PROJECT_DIR" || { echo "无法进入目录 $PROJECT_DIR"; exit 1; }

# 激活虚拟环境
source /root/miniconda3/etc/profile.d/conda.sh
# 激活环境
conda activate vnpy

# 运行Python脚本中的主函数
python -c "from works.legu import $MAIN_FUNCTION; $MAIN_FUNCTION()"

# 退出虚拟环境
conda activate base
