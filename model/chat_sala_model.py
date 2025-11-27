# =============================================================================
# MODEL - SALA DE CHAT
# =============================================================================
# Representa uma sala de chat privada entre dois usuários.

from dataclasses import dataclass
from datetime import datetime


@dataclass
class ChatSala:
    """
    Representa uma sala de chat privada entre dois usuários.

    O ID da sala segue o padrão: "menor_id_maior_id"
    Isso garante que dois usuários sempre tenham a mesma sala.

    Exemplo:
        Usuários com ID 3 e 7 sempre usam a sala "3_7"
        Usuários com ID 7 e 3 também usam a sala "3_7"

    Atributos:
        id: Identificador único da sala (formato "menor_id_maior_id")
        criada_em: Data/hora de criação da sala
        ultima_atividade: Data/hora da última mensagem enviada
    """
    id: str
    criada_em: datetime
    ultima_atividade: datetime

#### model/chat_mensagem_model.py

# =============================================================================
# MODEL - MENSAGEM DE CHAT
# =============================================================================
# Representa uma mensagem enviada em uma sala de chat.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ChatMensagem:
    """
    Representa uma mensagem enviada em uma sala de chat.

    Atributos:
        id: Identificador único da mensagem
        sala_id: ID da sala onde foi enviada
        usuario_id: ID do usuário que enviou
        mensagem: Conteúdo da mensagem
        data_envio: Data/hora do envio
        lida_em: Data/hora em que foi lida (None se não lida)
    """
    id: int
    sala_id: str
    usuario_id: int
    mensagem: str
    data_envio: datetime
    lida_em: Optional[datetime] = None


#### model/chat_participante_model.py

# =============================================================================
# MODEL - PARTICIPANTE DE CHAT
# =============================================================================
# Representa a participação de um usuário em uma sala de chat.

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ChatParticipante:
    """
    Representa a participação de um usuário em uma sala.

    Esta entidade relaciona usuários às suas salas de chat.
    A chave primária é composta por (sala_id, usuario_id).

    Atributos:
        sala_id: ID da sala de chat
        usuario_id: ID do usuário participante
        ultima_leitura: Data/hora da última leitura das mensagens
    """
    sala_id: str
    usuario_id: int
    ultima_leitura: Optional[datetime] = None