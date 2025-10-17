from dataclasses import dataclass
from typing import Optional
import uuid

from src.domain.seguradora import Seguradora
from src.domain.usuario import Usuario


@dataclass
class Pericia:

    def __init__(
        self,
        id: uuid.UUID,
        created_at: Optional[str] = None,
        data_empresa: Optional[str] = None,
        categoria: Optional[str] = None,
        tipo_vistoria: Optional[str] = None,
        causa: Optional[str] = None,
        numero_proposta: Optional[str] = None,
        cultura: Optional[str] = None,
        produtividade_esperada: Optional[str] = None,
        seguradora_scr: Optional[str] = None,
        numero_apolice: Optional[str] = None,
        segurado: Optional[str] = None,
        cpf_cnpj: Optional[str] = None,
        numero_contato: Optional[str] = None,
        municipio: Optional[str] = None,
        uf: Optional[str] = None,
        area: Optional[str] = None,
        nome_analista: Optional[str] = None,
        numero_sinistro: Optional[str] = None,
        data_captura: Optional[str] = None,
        status: Optional[str] = None,
        evento: Optional[str] = None,
        cobertura: Optional[str] = None,
        corretor: Optional[str] = None,
        usuario_id: uuid.UUID = None,
        seguradora_id: uuid.UUID = None,
        usuario: Optional["Usuario"] = None,
        seguradora: Optional["Seguradora"] = None
    ):
        self.id = id
        self.created_at = created_at
        self.data_empresa = data_empresa
        self.categoria = categoria
        self.tipo_vistoria = tipo_vistoria
        self.causa = causa
        self.numero_proposta = numero_proposta
        self.cultura = cultura
        self.produtividade_esperada = produtividade_esperada
        self.seguradora_scr = seguradora_scr
        self.numero_apolice = numero_apolice
        self.segurado = segurado
        self.cpf_cnpj = cpf_cnpj
        self.numero_contato = numero_contato
        self.municipio = municipio
        self.uf = uf
        self.area = area
        self.nome_analista = nome_analista
        self.numero_sinistro = numero_sinistro
        self.data_captura = data_captura
        self.status = status
        self.evento = evento
        self.cobertura = cobertura
        self.corretor = corretor
        self.usuario_id = usuario_id
        self.seguradora_id = seguradora_id
        self.usuario = usuario
        self.seguradora = seguradora