# syntax=docker/dockerfile:1

FROM ghcr.io/astral-sh/uv:python3.14-trixie AS builder

WORKDIR /build

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync \
        --frozen \
        --no-install-project \
        --no-editable \
        --compile-bytecode \
        --no-dev

FROM python:3.14-slim-trixie AS app

WORKDIR /app

COPY ./src/mba_dsa/ /app/mba_dsa/

COPY \
    --from=builder \
    --chown=app:app \
    /build/.venv/ \
    /app/.venv/

ENTRYPOINT [ "/app/.venv/bin/python"]

VOLUME ["/tmp/hf"]

CMD [ "-m", "mba_dsa" ]
