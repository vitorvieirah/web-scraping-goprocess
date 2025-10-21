from dataclasses import dataclass
from typing import Optional
from datetime import datetime

from src.domain.seguradora import Seguradora
from src.domain.usuario import Usuario


@dataclass
class Pericia:
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    seguradora: Optional[str] = None
    numero_proposta: Optional[str] = None
    numero_apolice: Optional[str] = None
    area_segurada_total: Optional[str] = None
    numero_sinistro: Optional[str] = None
    data_aviso_sinistro: Optional[str] = None
    data_ocorrencia: Optional[str] = None
    evento: Optional[str] = None
    cultura: Optional[str] = None
    produtividade_estimada: Optional[str] = None
    numero_aviso: Optional[str] = None
    cobertura_sinistrada: Optional[str] = None
    nome_proponente: Optional[str] = None
    telefone_proponente: Optional[str] = None
    cpf_cnpj_proponente: Optional[str] = None
    nome_corretor: Optional[str] = None
    usuario_id: Optional[int] = None
    seguradora_id: Optional[int] = None
    usuario: Optional["Usuario"] = None
    seguradora_rel: Optional["Seguradora"] = None

