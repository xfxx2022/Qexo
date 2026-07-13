import os


def vercel_analytics(request):
    """
    将 Vercel Analytics 开关暴露给所有模板（含 403/404/500 错误页）。

    默认行为：在 Vercel 生产环境（VERCEL 环境变量存在且为真）自动开启。
    可通过环境变量 VERCEL_ANALYTICS 强制覆盖：
        - 设为 true / 1 / yes  -> 强制开启
        - 设为 false / 0 / no  -> 强制关闭
        - 不设置               -> 仅在 Vercel 环境自动开启

    注意：与视图传入的 `settings` 变量（Qexo 配置 JSON）无冲突，
    此处使用独立变量名 VERCEL_ANALYTICS_ENABLED，避免覆盖模板中的 settings。
    """
    vercel_env = os.environ.get("VERCEL", "").lower() in ("1", "true")
    override = os.environ.get("VERCEL_ANALYTICS", "").lower()

    if override in ("0", "false", "no"):
        enabled = False
    elif override in ("1", "true", "yes"):
        enabled = True
    else:
        enabled = vercel_env

    return {"VERCEL_ANALYTICS_ENABLED": enabled}
