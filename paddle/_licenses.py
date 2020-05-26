import logging
from urllib.parse import urljoin

from .validators import validate_date

log = logging.getLogger(__name__)


def generate_license(
    self,
    product_id: int,
    allowed_uses: int,
    expires_at=None
) -> dict:
    url = urljoin(self.vendors_v2, 'product/generate_license')
    json = {
        'product_id': product_id,
        'allowed_uses': allowed_uses,
    }
    if expires_at:
        json['expires_at'] = validate_date(expires_at)
    return self.post(url=url)