```mermaid
flowchart TD
    Start([用户问题]) --> SafetyIn[安全大脑检测输入]
    SafetyIn --> Route{路由 & 分层}
    Route -->|简单问题| Direct[直接调用单个专家]
    Route -->|复杂问题| Multi[进入多大脑对话]

    subgraph MultiBrain [并行多大脑对话 共享框架]
        Init[初始化共享框架] --> Pick[随机选2-3个大脑]
        Pick --> Loop{循环 <上限?<br>未收敛?}
        Loop -->|是| Parallel[并行调用]
        
        subgraph Workers [ ]
            direction LR
            A[大脑A] --> A1[调用API]
            B[大脑B] --> B1[调用API]
            C[大脑C] --> C1[调用API]
        end
        
        Parallel --> Workers
        Workers --> Sync[同步点 等待全部完成]
        Sync --> SafetyMid[安全检测本轮输出]
        SafetyMid --> Merge[合并结果更新框架]
        Merge --> Loop
    end

    Loop -->|否| Aggregate[整合最终框架]
    Aggregate --> SafetyOut[安全检测最终输出]
    SafetyOut --> Final[最终答案]
    Final --> End([返回用户])
    Direct --> SafetyOut

    %% 添加三个警示节点，用虚线连接到相关位置
    Warning1[⚠️ 改进线程池！<br>否则资源爆炸！<br>考虑是否多进程包含多线程] -.-> Parallel
    Warning2[⏱️ 同步点记录耗时<br>超时则中断循环] -.-> Sync
    SafetyAll[🔒 安全大脑全覆盖<br>（输入/中间/输出）] -.-> SafetyIn
    SafetyAll -.-> SafetyMid
    SafetyAll -.-> SafetyOut
 ```