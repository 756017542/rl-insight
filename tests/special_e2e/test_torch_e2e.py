# Copyright (c) 2025 verl-project authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from pathlib import Path
from rl_insight.main import main


def test_torch_e2e_with_input_path(monkeypatch, tmp_path):
    # 定义输入输出目录（相对于当前工作目录）
    test_dir = Path(__file__).parent.parent.parent
    input_dir = test_dir / "torch_data"
    output_dir = tmp_path / "torch_output"

    # 确保输入目录存在
    assert input_dir.exists(), f"Input directory {input_dir} does not exist"

    # 设置命令行参数
    test_args = [
        "main.py",
        f"--input-path={input_dir}",
        f"--output-path={output_dir}",
        "--profiler-type=torch",  # 显式指定（默认 mstx）
        # 其他参数可按需添加，如 --vis-type=html（默认）、--rank-list=all（默认）
    ]
    monkeypatch.setattr(sys, "argv", test_args)

    # 执行主函数
    main()

    # 验证输出文件（生成 rl_timeline.html）
    output_file = output_dir / "rl_timeline.html"
    assert output_file.exists()
