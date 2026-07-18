import pandas as pd

def get_top_importance(model, X_train, top=15):
    """
    Расчет и ранжирование важности признаков (Feature Importance).
    
    Связывает скоры важности от обученной модели с именами колонок,
    сортирует их по убыванию и возвращает топ-N значимых фич.
    """
    importance = model.get_feature_importance()
    features_names = X_train.columns

    data_importance = pd.DataFrame({"features_names":features_names, "importance": importance})

    data_importance = data_importance.sort_values(by=["importance"])[::-1].reset_index(drop=True)

    return data_importance.head(top)



def event_features(new_train:pd.DataFrame, event:pd.DataFrame) -> pd.DataFrame:
    """
    Генерация динамических признаков из сырых поведенческих логов (events.csv).
    
    Фильтрует события строго до момента целевого действия (event_ts < assignment_ts)
    для защиты от утечки данных . Агрегирует метрики вовлеченности 
    (чаты, разброс цен, длительность и глубину сессий).
    """
    events_filtered = event.merge(
        new_train[["lead_id", "assignment_ts"]],
        on="lead_id",
        how="inner"
    )


    events_filtered = events_filtered[events_filtered["event_ts"] < events_filtered["assignment_ts"]]

    events_features = events_filtered.groupby("lead_id").agg(
        chat_open_count=("event_type", lambda x: (x=="chat_open").sum()),
        price_std=("item_price_log", "std"),
        price_spread=("item_price_log", lambda x: x.max() - x.min()),
        activity_duration_min=("event_ts", lambda x: (x.max() - x.min()).total_seconds()/60),
        unique_slots_count=('src_slot', 'nunique'),
        max_ctx_seq=('ctx_seq', 'count')
    ).reset_index()


    events_features["price_std"] = events_features["price_std"].fillna(0)

    new_train = new_train.merge(events_features, on='lead_id', how='left')
    cols_to_fill = ['chat_open_count', 'unique_slots_count', 'max_ctx_seq', 'price_spread', 'activity_duration_min']
    new_train[cols_to_fill] = new_train[cols_to_fill].fillna(0)
    return new_train