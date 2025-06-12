from fastapi import APIRouter

from product.health.health_env import health_settings
from product.health.service import check_cert, check_http, check_kafka, check_mongodb

router = APIRouter()


@router.get("/health")
async def health():
    result = {
        "self": {"status": "ok"},
        "kafka": await check_kafka(),
        "tlsCertificate": check_cert("certificate.crt"),
        "tlsKey": check_cert("key.pem"),
        "mongodb": await check_mongodb(),
    }

    # HTTP-basierte Checks
    for name, url in {
        "keycloak": health_settings.KEYCLOAK_HEALTH_URL,
        "prometheus": health_settings.PROMETHEUS_HEALTH_URL,
        "tempo": health_settings.TEMPO_HEALTH_URL,
    }.items():
        result.update(await check_http(name, url))

    return result
