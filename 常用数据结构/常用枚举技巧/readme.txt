一、枚举右维护左
    对于双变量问题：例如两数之和 ai + aj = t, 可以枚举右边的 aj, 转换成 单变量问题
    也就是在 aj 左边查找是否有 ai = t - aj, 可以用哈希表维护
    我把这个技巧叫做 枚举右，维护左

二、枚举中间
    对于三个或者四个变量的问题，枚举中间的变量往往更好计算