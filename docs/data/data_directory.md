# RL-Insight - 数据文件目录结构

## 一、采集Torch Profiling 数据目录结构

```
<profile-data-path>/
└── <role>/
    └── prof_*.json.gz
```

## 二、采集Mstx Profiling 数据目录结构

```
<profile-data-path>/
└── <role>/
    └── *_ascend_pt/
        |── profiler_info_*.json
        └── ASCEND_PROFILER_OUTPUT/
            └── trace_view.json
```