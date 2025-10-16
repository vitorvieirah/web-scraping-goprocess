from dataclasses import dataclass
from typing import Optional
import uuid




@dataclass
class Pericia:

    id: Optional[uuid.UUID] = None
    created_at: Optional[str] = None
    data_empresa: Optional[str] = None
    categoria: Optional[str] = None
    tipo_vistoria: Optional[str] = None
    causa: Optional[str] = None
    numero_proposta: Optional[str] = None
    cultura: Optional[str] = None
    produtividade_esperada: Optional[str] = None
    seguradora: Optional[str] = None
    numero_apolice: Optional[str] = None
    segurado: Optional[str] = None
    cpf_cnpj: Optional[str] = None
    numero_contato: Optional[str] = None
    municipio: Optional[str] = None
    uf: Optional[str] = None
    area: Optional[str] = None
    nome_analista: Optional[str] = None
    numero_sinistro: Optional[str] = None
    data_captura: Optional[str] = None
    status: Optional[str] = None
    evento: Optional[str] = None
    cobertura: Optional[str] = None
    corretor: Optional[str] = None