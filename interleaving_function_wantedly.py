from typing import List

def new_ranking(user_id: int, page: int, per_page: int) -> List[int]:
    ids = [i for i in range(1, 31)]  # 新しいアルゴリズムのダミー結果
    start = (page - 1) * per_page
    return ids[start:start + per_page]

def old_ranking(user_id: int, page: int, per_page: int) -> List[int]:
    ids = [30 - i for i in range(30)]  # 古いアルゴリズムのダミー結果（逆順）
    start = (page - 1) * per_page
    return ids[start:start + per_page]

def interleaving(user_id: int, page: int, per_page: int) -> List[int]:
    new_ids = new_ranking(user_id, 1, 1000)
    old_ids = old_ranking(user_id, 1, 1000)
    
    seen = set()
    result = []

    i = j = 0
    toggle = True  # new -> old -> new -> ...

    while len(result) < page * per_page and (i < len(new_ids) or j < len(old_ids)):
        if toggle and i < len(new_ids):
            if new_ids[i] not in seen:
                seen.add(new_ids[i])
                result.append(new_ids[i])
            i += 1
        elif not toggle and j < len(old_ids):
            if old_ids[j] not in seen:
                seen.add(old_ids[j])
                result.append(old_ids[j])
            j += 1
        toggle = not toggle

    start = (page - 1) * per_page
    return result[start:start + per_page]
