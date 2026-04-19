from polars import DataFrame
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer

from .tf_idf import tf_idf


def cluster_analysis(
    df: DataFrame,
    col_name: str,
    /,
    ngram_range: tuple[int, ...] | None = None,
    min_df: float | int = 5,
    max_df: float | int = 0.95,
    sublinear_tf: bool = True,
    pca_n_components: int = 2,
    kmeans_n_clusters: int = 3,
    random_state: int = 42,
    random_state_pca: int | None = None,
    random_state_kmeans: int | None = None,
) -> tuple[DataFrame, TfidfVectorizer, PCA, KMeans]:
    X_tfidf, vec = tf_idf(
        (_df := df.clone()).get_column(col_name),
        ngram_range=ngram_range,
        min_df=min_df,
        max_df=max_df,
        sublinear_tf=sublinear_tf,
    )

    pca_vecs = DataFrame(
        data=(
            pca_model := PCA(
                n_components=pca_n_components,
                random_state=random_state_pca or random_state,
            )
        ).fit_transform(X_tfidf),
        schema=[f"pca_{i}" for i in range(pca_n_components)],
    )

    clusters = DataFrame(
        data=(
            kmeans := KMeans(
                n_clusters=kmeans_n_clusters,
                random_state=random_state_kmeans or random_state,
            ).fit(X_tfidf)
        ).labels_,
        schema=["cluster"],
    )

    return (
        _df.hstack(pca_vecs).hstack(clusters),
        vec,
        pca_model,
        kmeans,
    )
